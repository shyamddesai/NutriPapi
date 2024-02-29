import { useMemo } from "react";
import styles from "./../../css/index/star-rating-section.module.css";

const StarRatingSection = ({
  nutriPapiHasHelpedMeBalan,
  paddyPimblett,
  fighter,
  ellipseShape,
  propLeft,
}) => {
  const ellipseShapeIconStyle = useMemo(() => {
    return {
      left: propLeft,
    };
  }, [propLeft]);

  return (
    <div className={styles.starRatingSection}>
      <div className={styles.starGroup}>
        <div className={styles.stars}>
          <img
            className={styles.starsChild}
            loading="lazy"
            alt=""
            src="/star-2.svg"
          />
          <img
            className={styles.starsItem}
            loading="lazy"
            alt=""
            src="/star-3.svg"
          />
          <img
            className={styles.starsInner}
            loading="lazy"
            alt=""
            src="/star-4.svg"
          />
          <img
            className={styles.starIcon}
            loading="lazy"
            alt=""
            src="/star-5.svg"
          />
          <img
            className={styles.starsChild1}
            loading="lazy"
            alt=""
            src="/star-6.svg"
          />
        </div>
      </div>
      <div className={styles.nutriPapiHas}>{nutriPapiHasHelpedMeBalan}</div>
      <div className={styles.testimonialContainer}>
        <div className={styles.paddyPimblett}>{paddyPimblett}</div>
        <div className={styles.testimonialContainerChild} />
        <div className={styles.fighter}>{fighter}</div>
      </div>
      <img
        className={styles.logo5ff3c18e1Icon}
        loading="lazy"
        alt=""
        src="/logo5ff3c18e-1.svg"
      />
      <img
        className={styles.ellipseShapeIcon}
        loading="lazy"
        alt=""
        src={ellipseShape}
        style={ellipseShapeIconStyle}
      />
    </div>
  );
};

export default StarRatingSection;
